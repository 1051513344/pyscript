

if __name__ == "__main__":

    className = "Work"

    rpcModel = """package com.bozhong.nursetransfer.service;

import com.bozhong.nursetransfer.common.dto.resp.{className}RespDTO;
import com.bozhong.nursetransfer.core.Result;
import java.util.List;
import java.util.Map;

/**
 * @author 徐顺洁
 * @date 2024年08月15日 14:22:26
 */
public interface {className}ReadServiceRPC {open}

    Result<List<{className}RespDTO>> listByWhere(Map<String, Object> params);

{close}""".format(className=className, open="{", close="}")
    with open(f"{className}ReadServiceRPC.java", "w", encoding='utf-8') as f:
        f.write(rpcModel)