# Change directory
setwd("~/papers/geo/imp/data")

# Read data from file
x = read.table("Gowalla_totalCheckins_1_million.txt")

# Get only latitude and longitude
y=data.frame(y$V3,y$V4)

#Write data to file
write.table(y, file="latlon.txt", row.names=FALSE, col.names=FALSE, sep=",")

# Read data from file
x = read.table("latlon.txt")

# Scatter Plot
plot(x, xlab="Latitude", ylab="Longitude")

