#include <assert.h>
#include <stdio.h>
#include "ringbuf.h"

int main(void)
{
    ringbuf_t rb;
    uint8_t v = 0u;

    ringbuf_init(&rb);
    assert(!ringbuf_get(&rb, &v));          /* empty buffer gives nothing */
    assert(ringbuf_put(&rb, 42u));
    assert(ringbuf_get(&rb, &v) && v == 42u);
    printf("test_ringbuf: PASS\n");
    return 0;
}
