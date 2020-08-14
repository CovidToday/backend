library(EpiEstim)
setwd(".")
df = read.csv("confirmed.csv")
epid.count = as.numeric(unlist(c(df['active'])))
window = 7
res.R = estimate_R(epid.count,method = "uncertain_si",config = make_config(list(t_start=2:(length(epid.count)-window),t_end=(2+window):length(epid.count),
                                                                                mean_si = 3.95, std_mean_si = 0.475,
                                                                                min_mean_si = 3.01, max_mean_si = 4.91,
                                                                                std_si = 1.51, std_std_si = 0.5575,
                                                                                min_std_si = 0.74, max_std_si = 2.97,
                                                                                n1 = 114, n2 = 114,mean_prior=2.6,std_prior=2)))
write.csv(res.R$R,'rtoutput.csv',row.names = TRUE)
