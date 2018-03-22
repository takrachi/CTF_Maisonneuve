#include <stdio.h>
#include <unistd.h>

int main() {
	for(int i=0; i<101; i++) {
		printf("\r[ Loading flag %d% ]", i);
		if (i%10==0)
			printf("  ^(;,;)^    ");
		else
			printf("  ^(:.:)^    ");
		fflush(stdout);
		usleep(45000);
	}

	printf("\n[+] DONE \n");
	sleep(1);
	printf("[*] J'espere que tu ne m'as pas execute ... FLAG_c2a8ebd5f2d48ab18bf3519316d0b489\n");
	return 0;
}

