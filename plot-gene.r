########################################################
##  plot genes or markers along each chromosome 

argv <- commandArgs(T)

library(ggplot2)

png(file=paste(argv[1],".png",sep=""),width=720,height=960)

md <- read.table(argv[1],header=T)

gn <- read.table("/brldata/home/ctan/ref/all/barley-chr.txt",header=T)

p0 <- ggplot() + geom_rect(data=gn,aes(xmin=0.5,xmax=1.5,ymin=0,ymax=len),fill="red") + scale_y_reverse()

p1 <- p0 + geom_segment(data=md,aes(x=smp-0.5,xend=smp+0.7,y=pos,yend=pos),color="green",size=1) + xlim(0,3)

p2 <- p1 + facet_wrap(~chr,ncol=4,scales="fixed")

p3 <- p2 + geom_text(data=md,aes(x=smp+1,y=pos,label=gene,vjust=0.5,hjust=0.25),color="blue",check_overlap=TRUE)

p3

dev.off()
