from v1.entities.textual.text.text_detection import TextDetection
from dateutil import parser


class LocationDetector(object):
    def __init__(self, entity_name, dictionary_name):
        self.text = ''
        self.text_dict = {}
        self.tagged_text = ''
        self.processed_text = ''
        self.location = []
        self.original_location_text = []
        self.text_detection_object = TextDetection(entity_name=entity_name)
        self.user_address = None
        self.user_lat_long = None
        self.user_location_updated_at = None

    def detect_location(self):
        """
        Takes a message and writtens the list of location present in the text
        :return: tuple (list of location , original text)
        """
        location_list = []
        original_list = []
        location_list, original_list = self.detect_location_format(location_list, original_list)
        return location_list, original_list

    def detect_entity(self, text=None, profile_check=True, user_address=None, user_lat_long=None,
                      user_location_updated=None):
        """
        Take text and returns location details
        :param text:
        :param profile_check:
        :param user_address:
        :param user_lat_long:
        :param user_location_updated:
        :return: tuple (list of location , original text)
        """
        if text:
            self.text = ' ' + text + ' '
            self.processed_text = self.text
            self.tagged_text = self.text

        self.profile_check = profile_check
        self.user_address = user_address
        self.user_lat_long = user_lat_long
        if user_location_updated:
            if not '+' in user_location_updated:
                space = user_location_updated.split(' ')
                if len(space) == 3:
                    user_location_updated = space[0] + ' ' + '+'.join(space[1:])
            self.user_location_updated_at = parser.parse(user_location_updated)
        else:
            self.user_location_updated_at = None
        location_data = self.detect_location()
        self.location = location_data[0]
        self.original_location_text = location_data[1]
        return location_data

    def detect_location_format(self, location_list=[], original_list=[]):
        """
        Detects location if it is present in the chat
        :param location_list:
        :param original_list:
        :return:
        """
        location_list_from_text_entity, original_list = self.text_detection_object.detect_entity(self.text)
        self.tagged_text = self.text_detection_object.tagged_text
        self.processed_text = self.text_detection_object.processed_text
        for location in location_list_from_text_entity:
            location_list.append(location)

        return location_list, original_list
