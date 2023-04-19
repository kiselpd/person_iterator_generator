def flat_generator(list_of_lists):
    for list_item in list_of_lists:
        for item in list_item:
            yield item


def improved_flat_generator(list_of_lists):
    for item in list_of_lists:
        if isinstance(item, list):
            for deep_item in improved_flat_generator(item):
                yield deep_item
        else:
            yield item


    






    



    