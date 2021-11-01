# coding: utf-8
#
# Licence : MIT Licence
# owner   : Fumiya Shibamata
# version : 2.0
# web : https://github.com/sbfm/ConfigController
#
import os
import configparser

class Call:
    """Configparser wrapper class.
    
    if there is no file or key, create it
    
    [sample code]
    import ConfigController as cc
    cini = cc.Call('config.ini')
    value = cini.getProperties("Application","setting","defaultValue")
    
    [sample code2]
    import ConfigController as cc
    cini = cc.Call('config.ini')
    cini.setSection("Application")
    value = cini.getProperties("setting","defaultValue")
    
    [sample code3]
    import ConfigController as cc
    cini = cc.Call('config.ini')
    cini.setSection("Application")
    value = cini.getPropertiesC("setting","defaultValue","settingInfoText")
    """
    
    config_ini = configparser.ConfigParser(comment_prefixes = "#", allow_no_value = True)
    
    def __init__(self,configFilePath = "config.ini", encoding = "utf-8"):
        """Set Config File Path.
        
        *argument
        [0]configFilePath
        """
        
        self.configFile = configFilePath
        # check has property file
        if not os.path.exists(configFilePath):
            # if property file is null make file
            f = open(configFilePath, 'w')
            f.close()
        self.config_ini.read(self.configFile, encoding)
    
    def setSection(self,sectionName):
        """Set section.
        
        this logic don't must use
        if you set a section, you will not need to set a section anymore.
        
        * argument
        [0] section name
        """
        self.sectionName = sectionName
        return 1
    
    def getProperties(self,*properties):
        """Get property value.
        
        If there is no value, a default is registered.
        
        * argument(Use setSection() in advance)
        [0] properties name
        [1] default value
        
        * argument2
        [0] section name
        [1] properties name
        [2] default value
        """
        
        if len(properties) == 2 :
            # set 2 arguments
            try :
                sectionName = self.sectionName
            except AttributeError as e:
                raise NameError("setSection() must be executed to pass 'sectionName'")
            
            propertiesName = properties[0]
            defaultValue = properties[1]
        elif len(properties) == 3 :
            # set 3 arguments
            sectionName = properties[0]
            propertiesName = properties[1]
            defaultValue = properties[2]
        else :
            raise TypeError("getProperties() mising required positional argument. ")
        
        # get properties.
        try :
            resultValue = self.config_ini[sectionName][propertiesName]
        except KeyError as e:
            # if there is no properties, get it after registering
            self.setProperties(sectionName,propertiesName,defaultValue)
            resultValue = self.config_ini[sectionName][propertiesName]
        return resultValue
    
    def getPropertiesC(self,*properties):
        """Get property value.
        
        If there is no value, a default is registered.
        
        * argument(Use setSection() in advance)
        [0] properties name
        [1] default value
        [2] properties comment
        
        * argument2
        [0] section name
        [1] properties name
        [2] default value
        [3] properties comment
        """
        
        if len(properties) == 3 :
            # set 3 arguments
            try :
                sectionName = self.sectionName
            except AttributeError as e:
                raise NameError("setSection() must be executed to pass 'sectionName'")
            
            propertiesName = properties[0]
            defaultValue = properties[1]
            defaultComment = properties[2]
        elif len(properties) == 4 :
            # set 4 arguments
            sectionName = properties[0]
            propertiesName = properties[1]
            defaultValue = properties[2]
            defaultComment = properties[3]
        else :
            raise TypeError("getProperties() mising required positional argument. ")
        
        # get properties.
        try :
            resultValue = self.config_ini[sectionName][propertiesName]
        except KeyError as e:
            # if there is no properties, get it after registering
            self.setComment(sectionName,defaultComment)
            self.setProperties(sectionName,propertiesName,defaultValue)
            resultValue = self.config_ini[sectionName][propertiesName]
        
        return resultValue
    
    def setComment(self,*properties):
        """Register properties Comment
        
        * argument(Use setSection() in advance)
        [0] default Comment
        
        * argument2
        [0] section name
        [1] default Comment
        """
        if len(properties) == 1 :
            # set 1 arguments
            try :
                sectionName = self.sectionName
            except AttributeError as e:
                raise NameError("setComment() must be executed to pass 'sectionName'")
            comment = properties[0]
            
        elif len(properties) == 2 :
            # set 2 arguments
            sectionName = properties[0]
            comment = properties[1]
            
        else :
            raise TypeError("setComment() mising required positional argument. ")
        
        # check section
        self.hasSection(sectionName)
        # wright properties file
        self.config_ini.set(sectionName, "# " + comment)
        with open(self.configFile, 'w') as file:
            self.config_ini.write(file)
        return 1
    
    def setProperties(self,*properties):
        """Register properties Value.
        
        * argument(Use setSection() in advance)
        [0] properties name
        [1] default value
        
        * argument2
        [0] section name
        [1] properties name
        [2] default value
        """
        if len(properties) == 2 :
            # set 2 arguments
            try :
                sectionName = self.sectionName
            except AttributeError as e:
                raise NameError("setProperties() must be executed to pass 'sectionName'")
            propertiesName = properties[0]
            setValue = properties[1]
            
        elif len(properties) == 3 :
            # set 3 arguments
            sectionName = properties[0]
            propertiesName = properties[1]
            setValue = properties[2]
        else :
            raise TypeError("setProperties() mising required positional argument. ")
        
        # check section
        self.hasSection(sectionName)
        # wright properties file
        self.config_ini.set(sectionName, propertiesName, setValue)
        with open(self.configFile, 'w') as file:
            self.config_ini.write(file)
        return 1

    def hasSection(self,sectionName):
        """Set section.  """
        if not(self.config_ini.has_section(sectionName)):
            self.config_ini.add_section(sectionName)
            with open(self.configFile, 'w') as file:
                self.config_ini.write(file)
        return 1
