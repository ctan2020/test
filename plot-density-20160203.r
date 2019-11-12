
library(ggplot2)

argv <- commandArgs(T)

png(file=paste(argv[1],".temp.png",sep=""),width=960,height=960)

p <- ggplot()

md <- read.table(argv[1],header=T)

p1 <- p + geom_point(data=md,aes(pos,log(num),color=factor(smp))) + labs(x="pos",y="log(del)")

p2 <- p1 + facet_wrap(~ chr,ncol=2,scales="free_x")

p2

dev.off()
