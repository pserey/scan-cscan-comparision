library(here)
library(readr)
scan <- read_tsv(here('tabela.tsv'))
library(ggplot2)
library(dplyr)

scan %>%
  ggplot()+
  geom_line(aes(x=input, y=scan, color="scan"))+
  geom_line(aes(x=input, y=cscan, color="cscan")) +
  theme_minimal()+
  scale_color_manual(values=c("blue", "red")) +
  labs(x="Input Size", y="Tempo de execução", color="Tipo de scan")
