########################################################
##  plot molecular marker in the chrs 

argv <- commandArgs(T)

library(ggplot2)

png(file=paste(argv[1],".png",sep=""),width=720,height=960)

md <- read.table(argv[1],header=T)

gn <- read.table("/brldata/home/ctan/ref/all/barley-chr.txt",header=T)

p0 <- ggplot() + geom_rect(data=gn,aes(xmin=1.0,xmax=2.0,ymin=0,ymax=len),fill="white")

p1 <- p0 + geom_segment(data=md,aes(x=1.0,xend=2.0,y=pos,yend=pos,color=log(num)),lwd = 2) + xlim(0,3)

p2 <- p1 + facet_wrap(~chr,ncol=4,scales="fixed") + scale_colour_gradient(limits=c(4,8),low="green",high="red")


p2

dev.off()
