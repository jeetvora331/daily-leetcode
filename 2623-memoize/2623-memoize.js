var memoize = (fn , cache = {}) =>
  (...args) =>
    cache[args.join()] ?? 
    (cache[args.join()] = fn(...args))
  


