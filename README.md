## Quickstart
Create images with Nginx and Redis from the tarred filesystem:
	
```shell
user@host $ docker import - orangetux/nginx < nginx/rootfs.tar
user@host $ docker import - orangetux/redis < redis/rootfs.tar
```

Now build the other images and run them by using `docker-compose`:

```shell
user@host $ docker-compose build
user@host $ docker-compose up
```

And head over `http://localhost:1337` and you should see an IP address.

