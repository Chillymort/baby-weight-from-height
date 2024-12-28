from sklearn import linear_model

x = [[20], [22], [24], [26], [28], [30], [32], [34], [36], [38]]
y = [7.5, 10, 12.5, 15, 19, 20, 24, 26, 30, 32]

reg = linear_model.LinearRegression()

reg = reg.fit(x, y)

height = int(input("What is the baby's length?"))

reg = reg.predict([[height]])[0]

print("%.2f" % reg + " lbs")