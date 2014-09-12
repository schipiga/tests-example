def test_mocking_example():
    user = User()
    mock = Mock()

    mock(user.is_registered, True)

    post = Post(title='my title', content='my content', user=user)
    post.save()

    assert_that(Post.objects.count(), 1)
