
class AppService():
    '''
        Class that hold all the methods from the app's business logic
    '''
    def __init__(self,
                 userRepository,
                 donationRepository,
                 bloodRequestRepository):
        self._userRepository = userRepository
        self._donationRepository = donationRepository
        self._bloodRequestRepository = bloodRequestRepository
