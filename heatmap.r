# Usage  R < heatmap.r --vanilla

    library(RColorBrewer)
    library(gplots)
		x=read.table("file_name", header=TRUE, )
		pdf("file_name.pdf", height=10, width=10)
		rownames(x)<-x[,1]
		x2<-x[,-1]
    		mat=data.matrix(x2)
	        heatmap.2(mat,
                Rowv=TRUE,
                Colv=TRUE,
                #dendrogram= c(none),
                distfun = dist,
                hclustfun = hclust,
                main = "Tick miRNA expression",
                xlab = "Samples", ylab = "miRNA",
                key=TRUE,
                keysize=1,
                trace="none",
                density.info=c("none"),
                margins=c(10, 8),
                col=greenred(75),
        	)
    
dev.off()


