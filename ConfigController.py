# coding: utf-8
#
# Licence : MIT Licence
# owner   : Fumiya Shibamata
#
import os
import configparser

class ConfigController:
    """configparser wrapper class
    
    if there is no file or key, create it
    
    [sample code]
    import ConfigController as cc
    cini = cc.ConfigController('config.ini')
    value = cini.getProperties("Application","setting","defaultValue")
    
    [sample code2]
    import ConfigController as cc
    cini = cc.ConfigController('config.ini')
    cini.setSection("Application")
    value = cini.getProperties("setting","defaultValue")
    """
    
    config_ini = configparser.ConfigParser()
    
    def __init__(self,configFilePath = "config.ini", encoding = "utf-8"):
        """set Config File Path
        
        *argument
        [0]configFilePath
        """
        # check has property file
        if not os.path.exists(configFilePath):
            # if property file is null make file
            f = open(configFilePath, "w")
            f.close()
        # read property file
        self.configFile = configFilePath
        self.config_ini.read(configFilePath, encoding)
    
    def setSection(self,sectionName):
        """set section
        
        this logic don't must use
        if you set a section, you will not need to set a section anymore.
        
        * argument
        [0] section name
        """
        self.sectionName = sectionName
        return 1
    
    def getProperties(self,*properties):
        """get property value
        
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
                print("error")
                return 0
            
            propertiesName = properties[0]
            defaultValue = properties[1]
        elif len(properties) == 3 :
            # set 3 arguments
            sectionName = properties[0]
            propertiesName = properties[1]
            defaultValue = properties[2]
        else :
            print("error")
            return 0
        # get properties.
        try :
            resultValue = self.config_ini[sectionName][propertiesName]
        except KeyError as e:
            self.setProperties(sectionName,propertiesName,defaultValue)
            resultValue = self.config_ini[sectionName][propertiesName]
        return resultValue

    def setProperties(self,*properties):
        """register properties Value
        
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
                print("Plese set section.")
                return 0
            propertiesName = properties[0]
            setValue = properties[1]
        elif len(properties) == 3 :
            # set 3 arguments
            sectionName = properties[0]
            propertiesName = properties[1]
            setValue = properties[2]
        else :
            print("error")
            return 0
        # check section
        self.hasSection(sectionName)
        # wright properties file
        self.config_ini.set(sectionName, propertiesName, setValue)
        with open(self.configFile, 'w') as file:
            self.config_ini.write(file)
        return 1

    def hasSection(self,sectionName):
        """set section
        """
        if not(self.config_ini.has_section(sectionName)):
            self.config_ini.add_section(sectionName)
            with open(self.configFile, 'w') as file:
                self.config_ini.write(file)
        return 1

