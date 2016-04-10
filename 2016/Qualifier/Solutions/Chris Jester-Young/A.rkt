#lang racket
(define (count-sheep n)
  (define number->set (compose list->set string->list number->string))
  (let loop ([remaining (number->set 1234567890)]
             [i n])
    (let ([next (set-subtract remaining (number->set i))])
      (if (set-empty? next)
          i
          (loop next (+ i n))))))

(for ([i (in-range (read))]
      [n (in-port)])
  (printf "Case #~a: ~a~%"
          (add1 i)
          (if (zero? n)
              "INSOMNIA"
              (count-sheep n))))
