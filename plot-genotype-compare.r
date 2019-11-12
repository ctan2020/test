########################################################
##  plot genotype difference along whole genome between two varieties 

argv <- commandArgs(T)

library(ggplot2)

png(file=paste(argv[1],".temp.png",sep=""),width=720,height=960)

md <- read.table(argv[1],header=T)

gn <- read.table("/brldata/home/ctan/ref/all/barley-chr.txt",header=T)

p0 <- ggplot() + geom_rect(data=gn,aes(xmin=0.5,xmax=2.5,ymin=0,ymax=len),fill="white")

p1 <- p0 + geom_rect(data=md,aes(xmin=smp-0.5,xmax=smp+0.5,ymin=pos,ymax=pos2,fill=log(num)))+scale_fill_gradient(limits=c(6,12),low = "#00FF00", high = "#FF3333", space = "Lab", na.value = "grey50",guide = "colourbar") + xlim(0,3)

p2 <- p1 + facet_wrap(~chr,ncol=4,scales="fixed")

p2

dev.off()
