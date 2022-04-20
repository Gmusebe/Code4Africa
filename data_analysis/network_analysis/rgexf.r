# Loading rgexf
library(rgexf)

# Accessing the path of the file
fn <- system.file("/home/musebe/code/Code4Africa/data/network_analysis/Network.gexf",
                     package = "rgexf")
lesmi <- read.gexf(fn)

# Taking a look at the first handful of nodes and edges
head(lesmi)