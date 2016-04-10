#lang racket
(define (count-runs str)
  (let loop ([runs 0]
             [last #\+]
             [i (sub1 (string-length str))])
    (if (negative? i)
        runs
        (let ([cur (string-ref str i)])
          (loop (if (char=? cur last) runs (add1 runs)) cur (sub1 i))))))

(for ([i (in-range (call-with-input-string (read-line) read))]
      [line (in-port read-line)])
  (printf "Case #~a: ~a~%" (add1 i) (count-runs line)))
