class TimeLimitedCache {
    cache = new Map()

    set (key, value, duration) {
      const cacheValue =    this.cache.get(key)
      if (cacheValue) {
          clearTimeout(cacheValue.timeoutId)
      }
        
      const timeoutId = setTimeout(()=>{
          this.cache.delete(key)
      }, duration)
    this.cache.set(key, {value,timeoutId})
        return !!cacheValue
    };

    
    get(key){
        if (this.cache.has(key)){
            return this.cache.get(key).value
        }
        return -1
    }
    
    count(){
        return this.cache.size
    }
}
