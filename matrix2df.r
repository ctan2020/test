
argv <- commandArgs(T) 

md <- as.matrix(read.table(argv[1],header=F))

rownames(md) <- c("AC","BD","EC2.1","EC2.2","EC7.1","EC7.2","W1","X1")

colnames(md) <- 1:ncol(md)

md2 <- as.data.frame(as.table(md))

md2$grp <- rep(ncol(md),8)

write.table(md2,paste(argv[1],".df",sep=""),quote=F,row.names=F,col.names=F)
