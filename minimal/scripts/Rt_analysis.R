library(EpiEstim)
setwd(".")
df = read.csv("dataset.csv")
epid.count = as.numeric(unlist(c(df['active'])))
window = 5
res.R = estimate_R(epid.count,method = "uncertain_si",config = make_config(list(t_start=2:(length(epid.count)-window),t_end=(2+window):length(epid.count),mean_si = 3.96, std_mean_si = 0.215,
                                                                                 min_mean_si = 3.53, max_mean_si = 4.39,
                                                                                 std_si = 4.75, std_std_si = 0.145,
                                                                                 min_std_si = 4.46, max_std_si = 5.07,
                                                                                 n1 = 468, n2 = 468,mean_prior=2.6,
                                                                                 std_prior=2)))
write.csv(res.R$R,'rtoutput.csv',row.names = TRUE)
