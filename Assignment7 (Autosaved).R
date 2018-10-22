#setwd("~/Desktop/INFO 3401/First Stuff/problem-set-7-josa5420")
#The above was for me to set the working directory to the right location

#6
#d <- read.csv(file="titanic.csv", head = TRUE, sep=",")
#print(d)
#summary(d)

#7
#print(names(d))
#print(names(d)[c(1,2)])
#t <- table(d$"Sex")

#8
#prop.table(table(d$"Survived")) #From this, we can see ~38.4% of people survived

#proportion_survived <- prop.table(table(d$"Sex",d$"Survived"))
#From this table, we can evaluate that if you were a woman, there was a ~74% chance of survival. If you were a man, there was a ~19% of surviving.

#9
#d$"minor"[d$"Age" >17] <- 0
#d$"minor"[d$"Age" <18] <- 1

#aggregate(Survived ~ minor + Sex,data = d,FUN = length)
#Using this table, 