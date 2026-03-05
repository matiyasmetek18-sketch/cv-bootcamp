import cv2 as cv
import json 
from basic_image_ops import check_if_valid
class PipelineExecutor:
    def __init__(self, config_path):
        '''
        This function loads and validates the config file
        It will call _load_config(self)
        It will initialzie space holders like self.original_image and
        self.processed_image
        
        :param self: an instance of this class
        :param config_path: is the config_path to be loaded and validated 
        '''
        self.config_path = config_path
        
        self._load_config()
        
        self.original_image = None
        self.processed_image = None
        
    def _load_config(self):
        '''
        This function opens the JSON file 
        It parses it into a python dictinoary 
        It validates required keys (input, output, operations)
        It validates types (operations must be a list, etc)
        It stores the config in self.config
        
        :param self: an instance of this class
        '''
        with open(self.config_path) as json_file:
            data = json.load(json_file)
                
            if 'input' not in data or 'output' not in data or 'operations' not in data:
                raise ValueError('Missing key in the JSON file')
            
            if 'visualize' not in data:
                data['visualize'] = {}
            
            operations = data['operations']
            
            if type(operations) is not list:
                raise ValueError('Operations is not a list')
            
            # checking if operations has only dictionaries
            for i in operations:
                if type(i) is not dict:
                    raise ValueError('This operation is not a dictionary')
                
                # chekcing to see if 'name' is in every dictionary
                if 'name' not in i:
                    raise ValueError('Missing \'name\' in the dictionaries')
            
            self.config = data
    
    def _load_image(self):
        '''
        This function should read and validate the image path 
        from self.config["input"]
        It stores self.original_image (the original/unchanged image) and 
        self.procesed_image
        
        :param self: an instance of this class
        '''
        self.original_image = cv.imread(self.config['input'])
        
        if self.original_image is None:
            raise ValueError('The image path in pipleline_executor is invalid')
        
        self.processed_image = self.original_image.copy()
        
    
    def _apply_operation(self, operation_dict):
        '''
        This function applies a single operation using the registry
        It extracts the "name". 
        It will also extract the parameters (anything except "name")
        
        :param self: an instance of this class
        :param operation_dict: is the operation dictionary of the config file 
        '''
        pass
    
    def _save_output(self):
        '''
        This function saves the final enhanced image to the output path 
        It will read the output path from the config
        It will save self.processed_image using cv.imwrite
        
        :param self: an instance of this class
        '''
        pass
    
    def _visualize(self):
        '''
        This function runs visualizations based on config flags 
        
        :param self: an instance of this class
        '''
        pass
    
    def run(self):
        '''
        This function will execute the full pipeline
        It will load the image, loop through operations, save the output 
        and visualize the results
        This is the only method the user calls 
        
        :param self: an instance of this class 
        '''
        pass