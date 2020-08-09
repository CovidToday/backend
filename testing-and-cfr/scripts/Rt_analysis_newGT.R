library(EpiEstim)
setwd(".")
df = read.csv("confirmed.csv")
epid.count = as.numeric(unlist(c(df['active'])))
window = 7
res.R = estimate_R(epid.count,method = "uncertain_si",config = make_config(list(t_start=2:(length(epid.count)-window),t_end=(2+window):length(epid.count),
                                                                                mean_si = 5.20, std_mean_si = 0.75,
                                                                                min_mean_si = 3.78, max_mean_si = 6.78,
                                                                                std_si = 1.72, std_std_si = 0.755,
                                                                                min_std_si = 0.91, max_std_si = 3.93,
                                                                                n1 = 40, n2 = 40,mean_prior=2.6,std_prior=2)))
write.csv(res.R$R,'rtoutput.csv',row.names = TRUE)
