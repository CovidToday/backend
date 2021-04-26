library(EpiEstim)
setwd(".")
df = read.csv("confirmed.csv")
epid.count = as.numeric(unlist(c(df['active'])))
window = 7
res.R = estimate_R(epid.count,method = "uncertain_si",config = make_config(list(t_start=2:(length(epid.count)-window),t_end=(2+window):length(epid.count),
                                                                                mean_si = 5.53, std_mean_si = 0.487,
                                                                                min_mean_si = 4.58, max_mean_si = 6.53,
                                                                                std_si = 3.47, std_std_si = 0.417,
                                                                                min_std_si = 2.59, max_std_si = 4.26,
                                                                                n1 = 114, n2 = 114,mean_prior=2.6,std_prior=2)))
write.csv(res.R$R,'rt_temp/rtoutput.csv',row.names = TRUE)
