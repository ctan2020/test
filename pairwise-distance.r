
argv<-commandArgs(T)
options(digits=4)
mydata0<-read.table(argv[1],header=T,na.strings="-",sep="\t")
mydata<-mydata0[,5:12]
num = length(mydata[1,])

pd <- matrix(0,nrow=num,ncol=num)
for (i in 1:num){
	for (j in 1:i){
		comp<- mydata[,i]==mydata[,j]
		comm <- length(na.omit(comp[comp==TRUE]))
		diffe <- length(na.omit(comp[comp==FALSE]))
		pd[i,j] <- diffe/(diffe + comm)
		pd[j,i] <- pd[i,j]
	}
}

a <- colnames(mydata)
for (i in 1:num){
	a[i]<-sprintf("%10s",a[i])
}
rownames(pd) <- a

write.table(pd,argv[2],sep="\t",quote=FALSE,na="NA",row.names=T,col.names=F)
