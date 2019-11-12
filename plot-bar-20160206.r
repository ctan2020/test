
argv <- commandArgs(T)

library(ggplot2)

png(paste(argv[1],".png",sep=""),width=480,height=960)

md <- read.table(argv[1],header=T)

p0 <- ggplot()

p1 <- p0 + geom_bar(data=md,aes(smp,fill=factor(acs),weight=perc))

p <- p1 + facet_wrap(~grp,ncol=1,scales="free")

p

dev.off()


