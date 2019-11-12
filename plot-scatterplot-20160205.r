###############################################
##    plot scatterplot (PCA)

argv <- commandArgs(T)

library(ggplot2)

png(file=paste(argv[1],".png",sep=""),width=560,height=480)

md <- read.table(argv[1],header=T)

p0 <- ggplot()

p1 <- p0 + geom_point(data=md,aes(xval,yval,color=grp,stat="identity",position="identity"),shape=3,size=4)

p2 <- p1 + geom_text(data=md,aes(label=id,x=xval+0.1,y=yval,color=grp),size=4)

p <- p2 + labs(x="1st component - 0.33",y="2nd component - 0.20")

p

dev.off()

