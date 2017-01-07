library("ggplot2")
library("dplyr")
library("reshape2")
data <- read.csv("2ptc.csv")[, -1]

data <- mutate(data, value = value * 360/(2*pi))

data <- dcast(data, pair_id + chain ~ angle, value.var = "value")


ggplot(data = data) +
  geom_point(aes(x = phi, y = psi, col = chain)) +
  facet_wrap( ~ chain) +
  scale_x_continuous(breaks = seq(-180, 180, 30))

