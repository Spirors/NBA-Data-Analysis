decdf <- function(x, baseline, treatment)  ecdf(baseline)(x) - ecdf(treatment)(x)

a <- c(100.2, 99.0, 95.6, 94.9, 94.8, 94.7, 94.2, 93.5, 93.3, 93.0, 92.9, 92.9, 92.8, 91.7, 91.6, 91.4, 91.2, 91.1, 90.4, 90.4, 89.7, 89.5, 89.0, 88.9, 88.3, 86.4, 86.4, 86.3, 81.9)
b <- c(109.4, 108.6, 106.9, 105.2, 105.1, 104.3, 103.6, 102.2, 101.7, 101.0, 100.9, 100.6, 100.3, 99.4, 99.3, 99.0, 98.4, 98.3, 98.1, 98.1, 97.8, 97.4, 97.0, 97.0, 96.1, 95.8, 95.1, 94.2, 93.9, 93.6)
c <- c(118.1, 117.7, 115.4, 115.2, 115.1, 114.7, 114.5, 114.4, 114.2, 114.0, 113.9, 113.3, 112.5, 112.4, 112.2, 111.8, 111.7, 111.7, 110.7, 110.7, 108.9, 108.0, 107.5, 107.3, 107.0, 105.7, 104.9, 104.6, 104.5, 103.5)
Fa <- ecdf(a)
Fb <- ecdf(b)
Fc <- ecdf(c)

plot(Fa, col='red', verticals = TRUE)
lines(Fb, col='blue', verticals = TRUE)

x <- c(a,b)
max(abs(Fa(x) - Fb(x))) # the points where Fa or Fb jump

d <- curve(decdf(x,a,b), from=min(a,b), to=max(a,b))

plot(Fb, col='blue', verticals = TRUE)
lines(Fc, col='green', verticals = TRUE)

x <- c(b,c)
max(abs(Fb(x) - Fc(x))) # the points where Fb or Fc jump

d <- curve(decdf(x,b,c), from=min(b,c), to=max(b,c))
