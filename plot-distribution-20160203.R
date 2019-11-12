#!/usr/bin/R.exe

mydata1<-as.matrix(read.table("2v7.fst",header=F))
mydata2<-as.matrix(read.table("ACvTB.fst",header=F))
mtx<-cbind(mydata1[,1],mydata2[,1])

png(file="test.png",width=400,height=350)

plot(0.1,0,main="Statistics of enviromental selection",bty="o",xlab="Fst",ylab="percentage",xlim=c(0.1,1),ylim=c(0,0.5),axes=F)

axis(side=1,at=seq(0.1,1,0.1),labels=seq(0.1,1,0.1))

axis(side=2,at=seq(0,0.5,0.1),labels=seq(0,0.5,0.1))

legend("topright",legend=c("EC2vEC7","ACvTB"),col=c("red","blue"),lty=1)

cols=c("red","blue")

for (x in 1:2){
	par(new=T)
	h<-hist(mtx[,x],plot=F); d<-density(mtx[,x])
	plot(x=d$x, y=d$y * length(x) * diff(h$breaks)[1],type="l",xlim=c(0.1,1),ylim=c(0,0.5),main="",axes=F,col=cols[x],xlab="",ylab="")
}

dev.off()
