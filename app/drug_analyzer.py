class DrugAnalyzer:
    def __init__(self, data):
        self.data = data
        self.dataset = []
        for list in self.data:
            self.dataset.append(list[0][0:3])

    def __add__(self, newdata):
        if len(newdata) < 4:
            raise ValueError
        if type(newdata[0]) != str:
            raise ValueError
        if type(newdata[1]) and type(newdata[2]) and type(newdata[3]) != float:
            raise ValueError
        self.data = self.data + [newdata]
        return self
    
    def verify_series(self, series_id: str, act_subst_wgt: float, act_subst_rate: float, allowed_imp: float): 
        serie = []
        weight = []
        active = []
        rate = []
        def impurities():
            impurities = sum(rate) < allowed_imp * sum(weight)
            return impurities

        def active_substance(difference):
            active_substance = act_subst_wgt * len(serie) - difference < sum(active) < act_subst_wgt * len(serie) + difference
            return active_substance

        if series_id not in self.dataset:
            raise ValueError(f' {series_id} series is not present within the dataset.')

        for pill in self.data:
            if pill[0][0:3] == series_id:
                serie.append(pill)
                weight.append(pill[1])
                active.append(pill[2])
                rate.append(pill[3])
        
        difference = (act_subst_wgt * len(serie)) * act_subst_rate
        
        return impurities() and active_substance(difference)