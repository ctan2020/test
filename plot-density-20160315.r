
library(ggplot2)

argv <- commandArgs(T)

png(file=paste(argv[1],".temp.png",sep=""),width=480,height=480)

p <- ggplot()

md <- read.table(argv[1],header=T)

motif <- factor(nchar(as.character(md[,4])))

p1 <- p + geom_freqpoly(data=md,mapping=aes(repeats,group=motif,color=motif),binwidth=1)

p1

dev.off()
