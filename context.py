class ManagePayment:
    """
    This is the context class of the strategy pattern.The Context defines the
     interface of interest to clients.
    We wont use a constructor in ManagePayment but instead we pass it in the
     static method that follows.
    """
    @staticmethod
    def executePurchase(payment , discount, total_cost):
        """
        static method of context class that will change this object's behavior.
        """ 
        if discount:
            return payment.payment_method_with_disc(discount , total_cost)
        else:
            return payment.payment_method(total_cost)
        
    
   
      


class Assistants_Catalogue:
    
    @staticmethod
    def showCatalogue(sorting_pattern , sort_by , value , summer_catalogue):
        z = f"{sort_by}"
        x = getattr(sorting_pattern , f"{z}")
        return x(summer_catalogue , value)

        #With the above function and getattr method we achieve the following example

        '''
        if sort_by == "asc" and value == "size":
            return sorting_pattern.asc_size(summer_catalogue)
        
        if sort_by == "desc" and value == "size":
            return sorting_pattern.desc_size(summer_catalogue)
        
        if sort_by == "asc" and value == "color":
            return sorting_pattern.asc_color(summer_catalogue)

        if sort_by == "desc" and value == "color":
            return sorting_pattern.desc_color(summer_catalogue)
        
        if sort_by == "asc" and value == "fabric":
            return sorting_pattern.asc_fabric(summer_catalogue)

        if sort_by == "desc" and value == "fabric":
            return sorting_pattern.desc_fabric(summer_catalogue)
        
        if sort_by == "asc" and value == "scf":
            return sorting_pattern.asc_sz_clr_fbrc(summer_catalogue)

        if sort_by == "desc" and value == "scf":
            return sorting_pattern.desc_sz_clr_fbrc(summer_catalogue)
        
        '''
   