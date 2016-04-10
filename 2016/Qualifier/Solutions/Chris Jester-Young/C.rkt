#lang racket
(require srfi/2 math/number-theory)

(define (try n)
  (let loop ([i 10]
             [result '()])
    (if (= i 1)
        result
        (let* ([num (string->number n i)]
               [divisor (car (prime-divisors num))])
          (if (= divisor num)
              #f
              (loop (sub1 i) (cons divisor result)))))))

(define (perform n j)
  (define 2^n-1 (arithmetic-shift 1 (- n 1)))
  (let loop ([i j]
             [seen (set)])
    (when (positive? i)
      (or
       (and-let* ([num (number->string (bitwise-ior (+ (random 2^n-1) 2^n-1) 1) 2)]
                  [(not (set-member? seen num))]
                  [divisors (try num)])
         (display num)
         (for ([divisor (in-list divisors)])
           (display #\space)
           (display divisor))
         (newline)
         (loop (sub1 i) (set-add seen num)))
       (loop i seen)))))

(for ([i (read)]
      [n (in-port)]
      [j (in-port)])
  (printf "Case #~a:~%" (add1 i))
  (perform n j))
