##################################################
##   plot counts such as histogram or density
##################################################

library(ggplot2)

argv <- commandArgs(T)


png(paste(argv[1],".png",sep=""),width=960,height=960)

md <- read.table(argv[1],header=T)
names(md)<-c("chr","pos","num","group")

p <- ggplot()

p1 <- p + geom_point(data=md,aes(pos,num),color="red") 
#p1 <- p + geom_line(data=md,aes(pos,log(num),color=factor(num2),shape=factor(num2)),alpha=0.8,) + scale_colour_manual(values = c("red","green","black", "blue"))

p2 <- p1 + facet_wrap(~chr,ncol=2,scales = "free_x")

p3 <- p2 + theme(axis.text.x = element_text(angle = 45)) + labs(x="position",y="num")

p3

dev.off()

