# This script is based on the tutorial from https://rcompanion.org/rcompanion/e_07.html


# ----------------------- library import ---------------------------

# Import libraries
library(sjPlot)
library(sjmisc)
library(sjlabelled)
require(ISLR)
library(car)
library(sjPlot)
library(PerformanceAnalytics)
library(lmtest)
library(psych)
library(dplyr)
library(caret)


#############################################################################
# =============================== data setup ================================
#############################################################################


# ----------------------- data import ---------------------------

# Read data file
mydata <- read.csv(file="C:\\Users\\Kai Suchanek\\Google Drive\\Uni\\12. Semester\\Studienarbeit\\3.) Programmieren\\9.) Datenanalyse/180903_Datensatz_mit_Selenium3.csv", header=TRUE, sep=";")
str(mydata)

test_data <- read.csv(file="C:\\Users\\Kai Suchanek\\Google Drive\\Uni\\12. Semester\\Studienarbeit\\3.) Programmieren\\9.) Datenanalyse/test_data_cleaned.csv", header=TRUE, sep=";")
str(test_data)


# ------------------------ data cleaning -------------------------


by_contest <- group_by(final_data_final, Contest)

# group data by contest
by_contest <- group_by(mydata, Contest)
by_contest

# see which contest have what kind of win/loose ratio
summary_contest_wins <- by_contest %>% summarise( win = length(which(Winorloose == 1)), loose = length(which(Winorloose == 0)), percentage = win/loose)
summary_contest_wins

# filter out the high ratio contests
filtered_contests <- filter(summary_contest_wins, percentage < 0.09)
filtered_contests <- subset(filtered_contests, select = -c(win))
filtered_contests <- subset(filtered_contests, select = -c(loose))
filtered_contests <- subset(filtered_contests, select = -c(percentage))
filtered_contests

# final dataframe 
cleaned_data <- semi_join(mydata, filtered_contests)
str(cleaned_data)


#############################################################################
# ========================= descriptive statistics ==========================
#############################################################################


# ----------------------- Correlation analysis ---------------------------

# create a new dataset
mydata_var <- cleaned_data

# get rid of the columns that are not needed
mydata_var <- subset(mydata_var, select = -c(Winorloose))
mydata_var <- subset(mydata_var, select = -c(Contest))
mydata_var <- subset(mydata_var, select = -c(User_page))
mydata_var <- subset(mydata_var, select = -c(Project_page))

# check data
str(mydata_var)
head(mydata_var)

# print the correlation between variables
print(chart.Correlation(mydata_var, 
                        method="pearson",
                        histogram=TRUE,
                        pch=13))

# summary with psych library
describe(mydata_var)


# ----------------------- Faktor analysis ---------------------------

# get rid of the moderator
mydata_var <- subset(mydata_var, select = -c(Schwierigkeitsgrad))

# KMO criteria estimation
KMO(mydata_var)$MSA

# number of latent variables
scree(mydata_var)

# Factoranalysis
Modell <- factanal(mydata_var, factors = 4, rotation = "varimax", scores = "Bartlett", lower = 0.01)

# Print model
Modell


#############################################################################
# ========================= inductive statistics ===========================
#############################################################################


# ----------------------- creating normal models ---------------------------

# Model 1
m1 <- glm(Winorloose ~ Schwierigkeitsgrad, data=cleaned_data)

# Model 2
m2 <- glm(Winorloose ~ Follower, data=cleaned_data)

# Model 3
m3 <- glm(Winorloose ~ Following, data=cleaned_data)

# Model 4
m4 <- glm(Winorloose ~ Anzahl.der.Projekte, data=cleaned_data)

# Model 5
m5 <- glm(Winorloose ~ Views, data=cleaned_data)

# Model 6
m6 <- glm(Winorloose ~ Likes, data=cleaned_data)

# Model 7
m7 <- glm(Winorloose ~ Kommentare, data=cleaned_data)

# Model 8
m8 <- glm(Winorloose ~ Anzahl.der.Wörter, data=cleaned_data)

# Model 9
m9 <- glm(Winorloose ~ Anzahl.der.Bilder, data=cleaned_data)

# Model 10
m10 <- glm(Winorloose ~ Vollständige.Beschreibung, data=cleaned_data)

# Model 11
m11 <- glm(Winorloose ~ Schwierigkeitsgrad + Follower + Following + Anzahl.der.Projekte + Views + Likes + Kommentare + 
            Anzahl.der.Wörter + Anzahl.der.Bilder + Vollständige.Beschreibung, data=cleaned_data)


# ----------------------- creating moderator models ---------------------------


# Model 12
m12 <- glm(Winorloose ~ Views +Schwierigkeitsgrad + Schwierigkeitsgrad:Views, data=cleaned_data)

# Model 13
m13 <- glm(Winorloose ~ Likes + Schwierigkeitsgrad + Schwierigkeitsgrad:Likes, data=cleaned_data)

# Model 14
m14 <- glm(Winorloose ~ Kommentare + Schwierigkeitsgrad + Schwierigkeitsgrad:Kommentare, data=cleaned_data)

# Model 15
m15 <- glm(Winorloose ~ Anzahl.der.Wörter + Schwierigkeitsgrad + Schwierigkeitsgrad:Anzahl.der.Wörter, data=cleaned_data)

# Model 16
m16 <- glm(Winorloose ~ Anzahl.der.Bilder + Schwierigkeitsgrad + Schwierigkeitsgrad:Anzahl.der.Bilder, data=cleaned_data)

# Model 17
m17 <- glm(Winorloose ~ Vollständige.Beschreibung + Schwierigkeitsgrad + Schwierigkeitsgrad:Vollständige.Beschreibung, data=cleaned_data)

# Model 18
m18 <- glm(Winorloose ~ Follower + Following + Anzahl.der.Projekte + Views + Likes + Kommentare + Anzahl.der.Wörter + Anzahl.der.Bilder + Vollständige.Beschreibung + 
             Schwierigkeitsgrad + Schwierigkeitsgrad:Views + Schwierigkeitsgrad:Likes + Schwierigkeitsgrad:Kommentare + Schwierigkeitsgrad:Anzahl.der.Wörter + 
             Schwierigkeitsgrad:Anzahl.der.Bilder + Schwierigkeitsgrad:Vollständige.Beschreibung, data=cleaned_data)



# ----------------------- print models ---------------------------

# print normal models
print(tab_model(m1,m8,m9,m10,m2,m3,m4,m5,m6,m7,m11, digits = 5, 
                use.viewer = FALSE, collapse.ci = TRUE, show.stat = FALSE, show.aic = TRUE))

#print moderator models
print(tab_model(m15,m16,m17,m12,m13,m14,m18, digits = 5, 
                  use.viewer = FALSE, collapse.ci = TRUE, show.stat = FALSE, show.aic = TRUE))


#------------------------ make predictions --------------------------


#build prediction model
predict <- predict(m18, test_data, type="response")


model_pred_win <- rep("0", 47)
model_pred_win[predict > 0.11]<-"1"
tab <- table(model_pred_win, test_data$Winorloose)
tab

# print classification error
1-sum(diag(tab))/sum(tab)

