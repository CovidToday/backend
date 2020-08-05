library("surveillance")
library(EpiEstim)

setwd(".")
df = read.csv("confirmed.csv")
epid.count = as.numeric(unlist(c(df['active'])))[1:(length(unlist(c(df['active']))))]

boot_unit = 10

#epid.count = rollmean(rollmean(epid.count,7),7)

#PMF of reporting lag
rt.pmf = as.numeric(unlist(c(read.csv("rtlag.csv")['pmf'])))
#PMF of the incubation time is an interval censored gamma distribution
dmax <- 14
inc.pmf <- c(0,(plnorm(1:dmax,1.621,0.418) - plnorm(0:(dmax-1),1.621,0.418))/plnorm(dmax,1.621,0.418))


sts_reporting <- new("sts", epoch=1:length(epid.count),observed=matrix(epid.count,ncol=1))

bpnp.control <- list(k=10,eps=rep(0.5,2),iter.max=rep(2000,2),B=boot_unit,hookFun=NULL,verbose=TRUE,eq3a.method="C")

sts.bp_onset <- backprojNP(sts_reporting, incu.pmf=rt.pmf, control=bpnp.control)


for(o in 1:boot_unit){
  onsets = round(sts.bp_onset@lambda[,,o])
  cum_onset = c(rep(c(1),times=length(onsets)-length(rt.pmf)),rev(cumsum(rt.pmf)))
  onsets = onsets + rnbinom(n=onsets+1,prob=cum_onset,size = length(onsets))
  onsets = onsets[1:(length(onsets)-3)]

  sts_onset <- new("sts", epoch=1:length(onsets),observed=matrix(onsets,ncol=1))
  sts.bp_infection <- backprojNP(sts_onset, incu.pmf=inc.pmf,control=bpnp.control)
  
  for(infec in 1:boot_unit){
    infections = round(sts.bp_infection@lambda[,,infec])
    cum_infection = c(rep(c(1),times=length(infections)-length(inc.pmf)),rev(cumsum(inc.pmf)))
    infections = infections + rnbinom(n=infections+1,prob=cum_infection,size = length(infections))
    infections = infections[1:(length(infections)-4)]
    
    window = 5
    res.R = estimate_R(infections,method = "uncertain_si",config = make_config(list(t_start=2:(length(infections)-window),t_end=(2+window):length(infections),
                                                                                    mean_si = 5.689114, std_mean_si = 2.954078,
                                                                                    min_mean_si = 1, max_mean_si = 32.68376,
                                                                                    std_si = 2.281811, std_std_si = 0.9146942,
                                                                                    min_std_si = 0.5725632, max_std_si = 9.369653,
                                                                                    n1 = 40, n2 = 40,mean_prior=2.6,std_prior=2)))
    #plot(res.R)
    write.csv(res.R$R,sprintf("rt_temp/rtoutput_%0.0f_%0.0f.csv", o, infec),row.names = TRUE)
  }
}


