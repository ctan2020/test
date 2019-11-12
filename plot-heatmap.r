
library(ggplot2)
#library(plyr)
library(scales)
library(reshape)
library(Heatplus)

argv <- commandArgs(T)

png(file=paste(argv[1],".png",sep=""))
par(mar = c(3,4,4,6),mgp=c(5,1,0))

md <- read.table(argv[1],header=T,row.names=1)

md <- as.matrix(md)

reg1 <- regHeatmap(md,breaks=20,dendrogram=list(clustfun=hclust,col=list(status="no")))

plot(reg1)

dev.off()
