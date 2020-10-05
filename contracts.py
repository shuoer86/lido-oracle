def get_validators_keys(spr_id, contract, provider):
    validators_keys_count = contract.functions.getTotalSigningKeyCount(spr_id).call(
        {'from': provider.eth.defaultAccount.address})
    validators_keys_list = []
    if validators_keys_count > 0:
        for index in range(validators_keys_count):
            validator_key = contract.functions.getSigningKey(spr_id, index).call(
                {'from': provider.eth.defaultAccount.address})
            validators_keys_list.append(validator_key[0])
            index += 1
    return validators_keys_list
