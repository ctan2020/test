

argv <- commandArgs(T)
md <- read.table(argv[1],header=F,na.string="-",sep="\t")
md <- as.matrix(md)
md[,4] <-log(as.numeric(md[,4]))
write.table(md,argv[2],sep="\t",row.names=F,col.names=F,quote=FALSE,na="NA")
