
var_density <- function(ifile){
	
	## genotype difference along whole genome between two varieties

	png(file=paste(ifile,".temp.png",sep=""),width=720,height=960)

	md <- read.table(ifile,header=T)

	gn <- read.table("/brldata/home/ctan/ref/all/barley-chr.txt",header=T)

	p0 <- ggplot() + geom_rect(data=gn,aes(xmin=0.5,xmax=2.5,ymin=0,ymax=len),fill="white")

	p1 <- p0 + geom_segment(data=md,aes(x=smp-0.5,xend=smp+0.5,y=pos,yend=pos,color=factor(log(num)))) + xlim(0,3)

	p2 <- p1 + facet_wrap(~chr,ncol=4,scales="fixed")

	p2

	dev.off()
}

library(ggplot2)
argv<-commandArgs(T)
var_density(argv[1])
