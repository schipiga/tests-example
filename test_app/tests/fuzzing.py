def test_fuzzing_example():
    report = Report()
    client = Client()
    for fuzz_data in ('ADFASDFasdf',
                      '!#$asDFAS@#$',
                      '(&0239289(*^23sdf'):
        response = client.post('/login', fuzz_data)
        report.add(response)

    report.publish()
