# GPS Trajectories
setwd("~/papers/geo/imp/data/Geolife Trajectories 1.3/Geolife Trajectories 1.3/Data/000/Trajectory")

# Read data
x = read.table("20081023025304.plt")

# Convert data to data frame
y = data.frame(x[1],x[2])

# Plot the data
plot(y, main="GPS-000-1", xlab="Latitude", ylab="Longitude")

# Save the data to the file
write.table(y, "1.txt", sep=",", row.names=FALSE, col.names=FALSE)

# Get all the files in a folder
files <- list.files(pattern="*.plt")

# Make coord and plots directory
dir.create("plots")
dir.create("coord")

# Loop through all the files and apply the function
count<-1
len = length(files)
for(i in 1:len) {
  x = read.csv(files[i],skip=6)
  y = data.frame(x[1],x[2])
  file_name<-paste("GPS-000",i,sep="-")
  png(paste("plots/",file_name, ".png", sep=""), width=454, height=360, units="px")
  plot(y, main=file_name, xlab="Latitude", ylab="Longitude")
  dev.off()
  write.table(y, paste("coord/",i,".txt", sep=""), sep=",", row.names=FALSE, col.names=FALSE)
}
