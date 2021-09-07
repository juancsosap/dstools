from sklearn.metrics import confusion_matrix

def get_metrics(model, X, Z, threshold=None, beta=0.5):
    '''Retrun Model Metrics'''
    if threshold:
        Z_predict = (model.predict_proba(X)[:, 1] >= threshold).astype('int')
    else:
        Z_predict = model.predict(X)
        
    tn, fp, fn, tp = confusion_matrix(Z, Z_predict).ravel()

    _tpr = tp / (tp + fn) # True Positive Rate (Sensitivity / Recall)
    _fnr = fn / (tp + fn) # False Negative Rate (1 - TPR)
    
    _tnr = tn / (tn + fp) # True Negative Rate (Specificity / Selectivity)
    _fpr = fp / (tn + fp) # False Positive Rate (1 - TNR)
    
    _ppv = tp / (tp + fp) # Positive Predictive Value (Precision)
    _fdr = fp / (tp + fp) # False Discovery Rate (1 - PPV)
    
    _npv = tn / (tn + fn) # Negative Predictive Value (1 - FOR)
    _for = fn / (tn + fn) # False Omission Rate (1 - NPV)
    
    accuracy = (tp + tn) / (tp + tn + fp + fn) 
    f_score = _ppv * _tpr / (beta * _ppv + (1 - beta) * _tpr)

    return _tpr, _tnr, _ppv, _npv, accuracy, f_score