
class Bagging:
    def __init__(self, x_train, x_test, y_train, y_test):
        self.xtrain = x_train
        self.x_test = x_test
        self.y_train = y_train
        self.y_test = y_train
        self.__bag_param = dict()
        self.__score = list()
        self.__classifier = set()
        
    def add_classifier(self, classifier):
        self.__classifier.append[classifier]


# get a list of models to evaluate
def get_models():
	models = dict()
	models['lr'] = LogisticRegression()
	models['knn'] = KNeighborsClassifier()
	models['cart'] = DecisionTreeClassifier()
	models['svm'] = SVC()
	models['bayes'] = GaussianNB()
	return models



def bagging(X_train, X_test, y_train, y_test,n_est):
    n_est=51
    estimators=range(1,n_est)
    decision_clf = DecisionTreeClassifier()
    scores1 = list()
    scores2 = list()
    
    for est in estimators:
        bagging_clf = BaggingClassifier(decision_clf, n_estimators=est, max_samples=0.67,max_features=0.67, 
                                    bootstrap=True, random_state=9)
        bagging_clf.fit(X_train, y_train)
        # test line
        y_pred_bagging1 = bagging_clf.predict(X_test)
        score_bc_dt1 = accuracy_score(y_test, y_pred_bagging1)
        scores1.append(score_bc_dt1)
        # train line
        y_pred_bagging2 = bagging_clf.predict(X_train)
        score_bc_dt2 = accuracy_score(y_train, y_pred_bagging2)
        scores2.append(score_bc_dt2)
    
    plt.figure(figsize=(10, 6))
    plt.title('Bagging Info')
    plt.xlabel('Estimators')
    plt.ylabel('Scores')
    plt.plot(estimators,scores1,'g',label='test line', linewidth=3)
    plt.plot(estimators,scores2,'c',label='train line', linewidth=3)
    plt.legend()
    plt.show()