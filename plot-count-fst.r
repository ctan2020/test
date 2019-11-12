##################################################
##   plot counts such as histogram or density
##################################################

library(ggplot2)

argv <- commandArgs(T)

png(paste(argv[1],".png",sep=""),width=960,height=960)

md <- read.table(argv[1],header=T)

md2 <- read.table(argv[1],header=T)
p <- ggplot()

p1 <- p + geom_line(data=md,aes(pos,log(num),color=factor(num2),shape=factor(num2)),alpha=0.8,) + scale_colour_manual(values = c("red","green","black", "blue"))

p2 <- p1 + facet_wrap(~chr,ncol=2,scales = "free_x")

p3 <- p2 + theme(axis.text.x = element_text(angle = 45)) + labs(x="position",y="log(num)")

p3

##################################################
##   plot counts such as histogram or density
##################################################
par(new=T)

library(ggplot2)

argv <- commandArgs(T)

#png(paste(argv[1],".png",sep=""),width=960,height=960)

md <- read.table("../fst/reseq-8-snp-fst.windowed.weir.fst",header=T)

p <- ggplot()

#p1 <- p + geom_point(data=md, aes(pos,log(num),color=smp))

p1 <- p + geom_line(data=md,aes(BIN_START,WEIGHTED_FST),color="blue") + geom_hline(yintercept=0.8,colour="red")

p2 <- p1 + facet_wrap(~CHROM,ncol=2,scales = "free_x")

p3 <- p2 + theme(axis.text.x = element_text(angle = 45)) + labs(x="position",y="Fst")

p3

dev.off()

