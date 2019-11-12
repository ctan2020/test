
argv <- commandArgs(T)

df <- read.table(argv[1],header=F,sep="\t")
vt <- c("Commander","Fleet","Hindmash","La_Trobe","Scope","Vlamingh","WI4304")

diff <- matrix(0,ncol=7,nrow=7)
rownames(diff) <- vt
colnames(diff) <- vt

comm <- matrix(0,ncol=7,nrow=7)
rownames(diff) <- vt
 
self <- numeric(7)
names(self) <- vt
 
for (i in 6:12){
	for (j in i:12){
	
		# get the diff variation
		d <- df[,i]!=df[,j]
		diff[i-4,j-4] <- length(d[d==TRUE])
		diff[j-4,i-4] <- diff[i-4,j-4]

		# get common variation
		c <- df[,i]==df[,j] && df[,i]!="2"
		comm[i-4,j-4] <- length(c[c==TRUE])
		comm[j-4,i-4] <- comm[i-4,j-4] 
	}
	# mutation number against morex
	s <- df[,i]!=2
	self[i-4] <- length(s[s==TRUE])
}

write.table(diff,argv[2],col.names=T,row.names=T)

write.table(comm,argv[2],col.names=T,row.names=T,append=T)

write.table(self,argv[2],append=T)
