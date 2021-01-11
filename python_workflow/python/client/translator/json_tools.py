'''
Created on Jan 11, 2021

@author: laurentmichel
'''

class JsonTools(object):
    '''
    classdocs
    '''


    @staticmethod
    def remove_key(dictionary, key):
        if  isinstance(dictionary, dict):
            return JsonTools.remove_dict_key(dictionary, key)
        elif  isinstance(dictionary, list):
            return JsonTools.remove_list_key(dictionary, key)
        raise Exception ("Unsupported type")
        
    @staticmethod
    def remove_dict_key(dictionary, key):
        """
        {key: {"A": "a", "B": "b"}}
            --> {"A": "a", "B": "b"}
        {key: [{"A1": "a", "B1": "b"}, {"A2": "a", "B2": "b"}]}
            --> [{"A1": "a", "B1": "b"}, {"A2": "a", "B2": "b"}]
        """
        if key not in dictionary:
            return dictionary
        if isinstance(dictionary[key], dict):
            return dictionary[key]
        elif isinstance(dictionary[key], list):
            return dictionary[key]
        raise Exception ("Unsupported type")
        
    @staticmethod
    def remove_list_key(dictionary, key):
        """
        [{key: {"A1": "a", "B1": "b"}}] 
            --> [{"A1": "a", "B1": "b"}]
        [{key: [{"A1": "a", "B1": "b"}, {"A2": "a", "B2": "b"}]}] 
            --> [{"A1": "a", "B1": "b"}, {"A2": "a", "B2": "b"}]
        """
        retour = []
        for item in dictionary:
            content = JsonTools.remove_dict_key(item, key)
            if isinstance(content, dict):
                retour.append(content)
            elif isinstance(content, list):
                retour = content
            else:
                raise Exception ("Unsupported type")
    
        return retour