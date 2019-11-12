
library(ggplot2)

argv <- commandArgs(T)

png(file=paste(argv[1],".temp.png",sep=""),width=960,height=960)

p <- ggplot()

md <- read.table(argv[1],header=T)

motif_len <- nchar(as.character(md[,4]))

p1 <- p + geom_bar(data=md,mapping=aes(x=chr,stat="count",fill=factor(motif_len))) + labs(x="Chr",y="Count")

p1

dev.off()
